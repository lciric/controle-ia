import sys
from transformers import AutoTokenizer
tok=AutoTokenizer.from_pretrained(sys.argv[1],local_files_only=True)
ids=tok.encode("COST: 12",add_special_tokens=False)
for f in (128009,128001,128008):
    print(f, repr(tok.convert_ids_to_tokens(f)), "décodage avec == sans :", tok.decode(ids+[f],skip_special_tokens=True)==tok.decode(ids,skip_special_tokens=True))
print("eos:",tok.eos_token, tok.eos_token_id)
