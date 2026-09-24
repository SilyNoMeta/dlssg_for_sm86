"""Extract the pinned runtime locally for Vulkan. Requires pefile; refuses overwrite."""
import argparse,hashlib
from pathlib import Path
import pefile
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--proxy',type=Path,required=True)
p.add_argument('--out',type=Path,required=True)
a=p.parse_args();pe=pefile.PE(str(a.proxy))
# The integrated proxy carries the unchanged upstream image as resource 31000.
for kind in pe.DIRECTORY_ENTRY_RESOURCE.entries:
    if kind.id==10:
        for item in kind.directory.entries:
            if item.id==31000:
                if len(item.directory.entries)!=1:raise RuntimeError('Ambiguous embedded proxy')
                d=item.directory.entries[0].data.struct
                pe=pefile.PE(data=pe.get_data(d.OffsetToData,d.Size))
                break
found=[]
for kind in pe.DIRECTORY_ENTRY_RESOURCE.entries:
    if kind.id!=10:continue
    for item in kind.directory.entries:
        if item.id!=30001:continue
        for lang in item.directory.entries:
            d=lang.data.struct;found.append(pe.get_data(d.OffsetToData,d.Size))
if len(found)!=1 or hashlib.sha256(found[0]).hexdigest()!='ff6e90eb78b827927dff5b4ecc6b1c870c2e9bca29ed9f48c7d348cc9e170b82':
    raise RuntimeError('Unsupported embedded NVIDIA runtime')
with a.out.open('xb') as f:f.write(found[0])
print(a.out)
