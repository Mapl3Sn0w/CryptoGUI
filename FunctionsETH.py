import hashlib
import binascii
import base58
import ecdsa
import codecs
from Crypto.Hash import keccak

def ripemd160(x):
    d = hashlib.new('ripemd160')
    d.update(x)
    return d
      
#Verify if WIF is valid by checking that the two checksums are equal  
def ValidateWIF(StringWIF):
    Step1 = (binascii.hexlify(base58.b58decode(StringWIF))).upper()
    Short1 = Step1[0:-8]
    
    StringShaX1 = (hashlib.sha256(binascii.unhexlify(Short1)).hexdigest()).upper()
    StringShaX2 = (hashlib.sha256(binascii.unhexlify(StringShaX1)).hexdigest()).upper()
    
    CheckSum1 = Step1[-8:].decode()
    CheckSum2 = StringShaX2[0:8]
    
    if CheckSum1==CheckSum2:
        return(True)
    else:
        return(False)

#convert WIF format to private key
def WIFtoPK(StringWIF):
    Step1 = (binascii.hexlify(base58.b58decode(StringWIF))).upper()
    Step2 = Step1[:-8]
    Step3 = Step2[2:]

    if StringWIF[0]=='K' or StringWIF[0]=='L':
        Step3=Step3[:-2]

    return(Step3.decode())

def WIFtoAddress(StringWIF):
    Address=PKtoAddress(WIFtoPK(StringWIF))
    return(Address)

def PKtoAddress(StringPK):
    Step1 = private_to_public(StringPK.upper())
    Step2 = public_to_address(Step1)
    return(Step2)

#################################################################################################
#FROM: https://github.com/Destiner/blocksmith/blob/master/blocksmith/ethereum.py ################
#################################################################################################

def private_to_public(private_key):
    private_key_bytes = codecs.decode(private_key, 'hex')
    # Get ECDSA public key
    key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
    key_bytes = key.to_string()
    public_key = codecs.encode(key_bytes, 'hex')
    return public_key

def public_to_address(public_key):
    public_key_bytes = codecs.decode(public_key, 'hex')
    keccak_hash = keccak.new(digest_bits=256)
    keccak_hash.update(public_key_bytes)
    keccak_digest = keccak_hash.hexdigest()
    # Take last 20 bytes
    wallet_len = 40
    wallet = '0x' + keccak_digest[-wallet_len:]
    return wallet
#################################################################################################