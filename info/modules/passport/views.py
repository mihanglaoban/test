from flask import request, abort, current_app, make_response

from info import redis_store, constants
from info.utils.captcha.captcha import captcha
from . import passport_blue


# @passport_blue.route("/sms_code", method=["POST"])
# def send_sms_code():




@passport_blue.route("/image_code")
def get_image_code():
    image_code_id = request.args.get("imageCodeId", None)

    if not image_code_id:
        return abort(403)

    name, text, image = captcha.generate_captcha()

    try:
        redis_store.set("ImageCodeId_" + image_code_id, text, constants.IMAGE_CODE_REDIS_EXPIRES)
    except Exception as e:
        current_app.logger.error(e)
        abort(500)

    response = make_response(image)
    response.headers['Content-Type'] = "image/jpg"
    return response
