import unittest
from mlflow_oidc_auth.entities import User, ExperimentPermission, RegisteredModelPermission, Group

class TestUser(unittest.TestCase):
    user_json = {
            "id": "123",
            "username": "test_user",
            "is_admin": True,
            "display_name": "Test User",
            "experiment_permissions": [{"experiment_id": "exp1", "permission": "read", "user_id": None, "group_id": None}],
            "registered_model_permissions": [{"name": "model1", "permission": "write", "user_id": None, "group_id": None}],
            "groups": [{"id": "group1", "group_name": "Group 1"}]
        }

    def test_user_to_json(self):
        user = User(
            id_=self.user_json["id"],
            username=self.user_json["username"],
            password_hash="password",
            is_admin=self.user_json["is_admin"],
            display_name=self.user_json["display_name"],
            experiment_permissions=[ExperimentPermission(x['experiment_id'], x['permission']) for x in self.user_json["experiment_permissions"]],
            registered_model_permissions=[RegisteredModelPermission(x['name'], x['permission']) for x in self.user_json["registered_model_permissions"]],
            groups=[Group(x['id'], x['group_name']) for x in self.user_json["groups"]]
        )

        self.assertEqual(user.to_json(), self.user_json)

    def test_user_from_json(self):
        user = User.from_json(self.user_json)

        self.assertEqual(user.id, self.user_json['id'])
        self.assertEqual(user.username, self.user_json['username'])
        self.assertEqual(user.password_hash, User.PASSWORD_HASH_REPR)
        self.assertEqual(user.is_admin, self.user_json['is_admin'])
        self.assertEqual(user.display_name, self.user_json['display_name'])
        for i, ep in enumerate(user.experiment_permissions):
            self.assertEqual(ep.experiment_id, self.user_json['experiment_permissions'][i]['experiment_id'])
            self.assertEqual(ep.permission, self.user_json['experiment_permissions'][i]['permission'])
        for i, rmp in enumerate(user.registered_model_permissions):
            self.assertEqual(rmp.name, self.user_json['registered_model_permissions'][i]['name'])
            self.assertEqual(rmp.permission, self.user_json['registered_model_permissions'][i]['permission'])
        for i, g in enumerate(user.groups):
            self.assertEqual(g.id, self.user_json['groups'][i]['id'])
            self.assertEqual(g.group_name, self.user_json['groups'][i]['group_name'])