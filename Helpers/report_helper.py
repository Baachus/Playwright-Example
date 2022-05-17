import pytest 
from jinja2 import Template

@pytest.mark.optionalhook
def pytest_reporter_context(context, config):
	context["title"] = "name"


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item: Any) -> Generator[None, Any, None]:
#     if rep.when == 'call' and rep.failed is True:
#         rep.extra = [
#             {
#                 "name": "Screenshot",
#                 "format": "image",
#                 "content": os.path.join(os.getcwd(), "reports", slugify(rep.nodeid), f"{item.name}.png"),
#             },
#             {
#                 "name": "Recording",
#                 "format": "video",
#                 "content": os.path.join(os.getcwd(), "reports", slugify(rep.nodeid), f"{item.name}.webm"),
#             },
#         ]