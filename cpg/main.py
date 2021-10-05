from cpg.CharBuilder import CharBuilder
import os

os.chdir('data')
for i in range(1, 2501):
    builder_latin = CharBuilder("Latin")
    builder_latin.build()
    dirname = None
    if builder_latin.character == builder_latin.character.lower():
        dirname = builder_latin.character
    elif builder_latin.character == builder_latin.character.upper():
        dirname = builder_latin.character.lower() + "_upper"

    if os.path.isdir(dirname):
        builder_latin.save(f'{dirname}/lpic{i}.jpeg')
    else:
        os.mkdir(dirname)
        builder_latin.save(f'{dirname}/lpic{i}.jpeg')

    image_jpeg = builder_latin.base64()
    image_png = builder_latin.base64(image_format='PNG')


for i in range(1, 2501):
    builder_greek = CharBuilder("Greek")
    builder_greek.build()
    dirname = builder_greek.character

    if os.path.isdir(dirname):
        builder_greek.save(f'{dirname}/gpic{i}.jpeg')
    else:
        os.mkdir(dirname)
        builder_greek.save(f'{dirname}/gpic{i}.jpeg')

    image_jpeg = builder_greek.base64()
    image_png = builder_greek.base64(image_format='PNG')
