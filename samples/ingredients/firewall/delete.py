#  Copyright 2022 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
from google.cloud import compute_v1


# <INGREDIENT delete_firewall_rule>
def delete_firewall_rule(project_id: str, firewall_rule_name: str):
    """
    Deleted a firewall rule from the project.

    Args:
        project_id: project ID or project number of the Cloud project you want to use.
        firewall_rule_name: name of the firewall rule you want to delete.
    """
    firewall_client = compute_v1.FirewallsClient()
    operation = firewall_client.delete_unary(
        project=project_id, firewall=firewall_rule_name
    )

    operation_client = compute_v1.GlobalOperationsClient()
    operation_client.wait(project=project_id, operation=operation.name)
    return
# </INGREDIENT>
