class Solution:

    def encode(self, strs: List[str]) -> str:
        enc=''
        for i in strs:
            enc+= str(len(i))+'#'+i
        return enc
    def decode(self, s: str) -> List[str]:
        dec=[]
        i=0
        while i < len(s):
            j=i
            while s[j]!='#':
                j+=1
            lngth = int(s[i:j])
            i=j+1
            dec.append(s[i:i+lngth])
            i+=lngth
        return dec
