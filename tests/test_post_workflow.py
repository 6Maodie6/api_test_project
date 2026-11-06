
import allure


@allure.feature("文章管理模块")
@allure.story("文章查询流程")
@allure.title("查询文章列表并获取文章详情")
def test_get_post_workflow(api_client):

    with allure.step("步骤1：获取文章列表"):
        list_response = api_client.get("/posts")
        assert list_response.status_code == 200

        posts = list_response.json()
        assert len(posts) > 0

    with allure.step("步骤2：提取文章ID"):
        post_id = posts[0]["id"]

    with allure.step("步骤3：根据ID查询文章详情"):
        detail_response = api_client.get(f"/posts/{post_id}")
        assert detail_response.status_code == 200

        detail = detail_response.json()

    with allure.step("步骤4：验证数据一致性"):
        assert detail["id"] == post_id
        assert detail["title"] == posts[0]["title"]
        assert detail["body"] == posts[0]["body"]
