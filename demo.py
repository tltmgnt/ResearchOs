import json
from researchos import Claim, Evidence, EpistemicController, Status

controller = EpistemicController()
controller.register(Claim('K1', 'Every prime number is odd'))
controller.transition('K1', Status.UNVERIFIED)
controller.add_evidence('K1', Evidence('E1', 'Counterexample: 2 is prime and even', supports=False, independently_verified=True))
print('Final status:', controller.claims['K1'].status.value)
print(json.dumps(controller.audit, indent=2))
