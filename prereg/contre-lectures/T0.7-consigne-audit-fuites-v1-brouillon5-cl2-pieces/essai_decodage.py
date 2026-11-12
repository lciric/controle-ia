import sys,warnings,logging
from transformers import AutoTokenizer
import transformers
tok=AutoTokenizer.from_pretrained(sys.argv[1],local_files_only=True)
print(type(tok).__name__, transformers.__version__, "clean_up attr:",getattr(tok,"clean_up_tokenization_spaces",None))
fins=[tok.convert_tokens_to_ids(x) for x in ("<|eot_id|>","<|end_of_text|>","<|eom_id|>")]
print("fins",fins,"spéciaux:",[i in tok.all_special_ids for i in fins])
cas=["ACTION: ADD\nTITLE: A test , with spaces .\nCOST: 1 200 GPU-hours\nPREDICTION: we don 't know ; it 's 3 x 400 !",
     "do n't  stop ' s ( x ) , y . z ? !  'm 're 've n't 'll"]
for t in cas:
    ids=tok.encode(t,add_special_tokens=False)
    a=tok.decode(ids,skip_special_tokens=True)
    b=tok.decode(ids,skip_special_tokens=True,clean_up_tokenization_spaces=True)
    c=tok.decode(ids,skip_special_tokens=True,clean_up_tokenization_spaces=False)
    d=tok.decode(ids+[fins[0]],skip_special_tokens=True)
    print("défaut==texte",a==t,"| nettoyage demandé==défaut",b==a,"| sans nettoyage==défaut",c==a,"| avec jeton de fin == sans",d==a)
