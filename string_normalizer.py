from unicodedata import normalize, is_normalized


class StringNormalizer:

    def normalize_to_nfd(self,text:str):
        return normalize('NFD',text)
    
    def normalize_to_nfc(self,text:str):
        return normalize('NFC',text)
    
    def normalize_to_nfkd(self,text:str):
        return normalize('NFKD',text)
    
    def normalize_to_nfkc(self,text:str):
        return normalize('NFKC',text)
    
    def is_normalized(self,text:str, normalization_form):
        return is_normalized(normalization_form,text)
    
    def normalize_all_forms(self,text:str):
        return{
            form:normalize(form,text) for form in ('NFD','NFC','NFKD','NFKC')
        }
    def to_unicode(self,text:str):
        return [f"U+{ord(char):04X}" for char in text]
    
# Função de comparação de strings com normalização
def compare_strings(str1, str2, normalization_form='NFC'):
        normalizer = StringNormalizer()
        
        # Normaliza ambas as strings na forma especificada
        if normalization_form == 'NFD':
            normalized_str1 = normalizer.normalize_to_nfd(str1)
            normalized_str2 = normalizer.normalize_to_nfd(str2)
        elif normalization_form == 'NFC':
            normalized_str1 = normalizer.normalize_to_nfc(str1)
            normalized_str2 = normalizer.normalize_to_nfc(str2)
        elif normalization_form == 'NFKD':
            normalized_str1 = normalizer.normalize_to_nfkd(str1)
            normalized_str2 = normalizer.normalize_to_nfkd(str2)
        elif normalization_form == 'NFKC':
            normalized_str1 = normalizer.normalize_to_nfkc(str1)
            normalized_str2 = normalizer.normalize_to_nfkc(str2)
        else:
            raise ValueError("Forma de normalização inválida. Escolha entre 'NFD', 'NFC', 'NFKD', ou 'NFKC'.")

        # Compara as strings normalizadas
        return normalized_str1 == normalized_str2

if __name__=='__main__':
    # Exemplo de uso
    normalizer = StringNormalizer()

    texto = "Café ç%$#@*&"
    unicode_codes = normalizer.to_unicode(texto)

    # Normalizações
    nfd = normalizer.normalize_to_nfd(texto)
    nfc = normalizer.normalize_to_nfc(texto)
    nfkd = normalizer.normalize_to_nfkd(texto)
    nfkc = normalizer.normalize_to_nfkc(texto)

    print("Original:", texto,normalizer.to_unicode(texto))
    print("NFD:", nfd,normalizer.to_unicode(nfd))
    print("NFC:", nfc,normalizer.to_unicode(nfc))
    print("NFKD:", nfkd,normalizer.to_unicode(nfkd))
    print("NFKC:", nfkc,normalizer.to_unicode(nfkc))

    # Verificação de normalização
    print("Está em NFC?", normalizer.is_normalized(texto, 'NFC'))
    print("Está em NFD?", normalizer.is_normalized(texto, 'NFD'))

    # Normalizando em todas as formas
    print("All forms:",normalizer.normalize_all_forms(texto))

    # Café representado com unicodes diferentes
    str1 = "Café"  # com acento agudo
    str2 = "Café"  # "é" representado como "e" + acento separado

    if str1 != str2:
        print('Não são iguais')
        print('str1: ',normalizer.to_unicode(str1))
        print('str2: ',normalizer.to_unicode(str2))

    # Comparação usando a forma NFC
    if compare_strings(str1, str2, normalization_form='NFC'):
        print("As strings são equivalentes após normalização em NFC.")
    else:
        print("As strings NÃO são equivalentes após normalização em NFC.")

    # Comparação usando a forma NFD
    if compare_strings(str1, str2, normalization_form='NFD'):
        print("As strings são equivalentes após normalização em NFD.")
    else:
        print("As strings NÃO são equivalentes após normalização em NFD.")
