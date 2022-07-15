# Face Count API

Helps to count number of faces in an Image.

### Requirements: 

Requirements can be found in `requirements.txt` file.

For installation run:

    pip install -r requirements.txt

### API's

- **countFace**: Requires two keys, refrence id, base 64 image.
    
        {
        "ref": <REFERENCE_ID>,
        "img": "BASE_64_Image"
        }

- **getCountByUrl**: Requires two keys, reference id and image path.

        {
        "ref": <REFERENCE_ID>,
        "url": "IMAGE_URL"
        }


