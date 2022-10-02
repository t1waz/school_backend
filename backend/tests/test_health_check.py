from starlette.testclient import TestClient
from main import app
import constants


test_app = TestClient(app=app)


class TestHealthCheckEndpoint:
    def test_get_request_on_health_check_endpoint(self):
        response = test_app.get(url=constants.HEALTH_CHECK_ENDPOINT)

        assert response.status_code == 200

    def test_post_request_on_health_check_endpoint(self):
        response = test_app.post(url=constants.HEALTH_CHECK_ENDPOINT)

        assert response.status_code != 200

    def test_patch_request_on_health_check_endpoint(self):
        response = test_app.patch(url=constants.HEALTH_CHECK_ENDPOINT)

        assert response.status_code != 200

    def test_delete_request_on_health_check_endpoint(self):
        response = test_app.delete(url=constants.HEALTH_CHECK_ENDPOINT)

        assert response.status_code != 200
