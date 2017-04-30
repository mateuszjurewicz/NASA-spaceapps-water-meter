# Python 3.6.1
# GRABS A LINK TO AN IMAGE AND USES EXTERNAL OCR API TO RETURN THE TEXT
# PROVIDE THE LINK AS FIRST COMMAND LINE ARGUMENT

# Works on this example input:
# http://www.smarthomewaterguide.org/images/water_meter_analog.jpg

# thanks to use 'Zaargh' for providing baseline
# https://github.com/Zaargh/ocr.space_code_example/blob/master/ocrspace_example.py

import requests
import json

def ocr_space_file(filename, overlay=False, api_key='a2b94ede3488957', language='eng'):
    """ OCR.space API request with local file.
        Python3.6
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to current key (500 usage)
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


def ocr_space_url(url, overlay=False, api_key='a2b94ede3488957', language='eng'):
    """ OCR.space API request with remote file.
        Python3.6
    :param url: Image url.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to current key (500 usage)
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content.decode()


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("linked_image", help="echo the image-link you wish to use")
    args = parser.parse_args()

    # Use examples:
    # test_file = ocr_space_file(filename='How-to-Read-Your-Meter.jpg', language='pol')
    test_url = ocr_space_url(args.linked_image)
    # load the string to json
    json1_data = json.loads(test_url)

    # their json structure is weeeeird...
    print(json1_data['ParsedResults'][0]['ParsedText'][:4])
