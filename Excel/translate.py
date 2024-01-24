from googletrans import Translator

translator = Translator(service_urls=['translate.google.com'])

# Dịch từ tiếng Hàn sang tiếng Anh
translation = translator.translate('안녕하세요.', dest='en')
print(translation.text)

# Dịch từ tiếng Hàn sang tiếng Nhật
translation = translator.translate('안녕하세요.', dest='ja')
print(translation.text)

# Dịch từ tiếng Latin sang tiếng Anh
translation = translator.translate('veritas lux mea', src='la', dest='en')
print(translation.text)