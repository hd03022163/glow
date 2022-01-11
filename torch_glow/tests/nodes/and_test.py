# Copyright (c) Glow Contributors. See CONTRIBUTORS file.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import, division, print_function, unicode_literals

import torch
from tests import utils


class SimpleAndModule(torch.nn.Module):
    def __init__(self):
        super(SimpleAndModule, self).__init__()

    def forward(self, a, b):
        c = a & b
        return torch.logical_or(c, b)


class TestAnd(utils.TorchGlowTestCase):
    @utils.deterministic_expand(
        [
            lambda: (
                "basic",
                torch.tensor([True, True, False, False], dtype=torch.bool),
                torch.tensor([True, False, True, False], dtype=torch.bool),
            ),
            lambda: (
                "basic_3d",
                torch.zeros((3, 4, 5), dtype=torch.bool),
                torch.ones((3, 4, 5), dtype=torch.bool),
            ),
            lambda: (
                "broadcast_3d",
                torch.zeros((3, 4, 5), dtype=torch.bool),
                torch.ones((4, 5), dtype=torch.bool),
            ),
        ]
    )
    def test_and(self, _, a, b, skip_to_glow=False):
        utils.run_comparison_tests(
            SimpleAndModule(),
            (a, b),
            fusible_ops={"aten::__and__"},
            skip_to_glow=skip_to_glow,
        )
