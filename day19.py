from fileOps import readFile

class rule:
    # Three examples:
        # a<2006:qkq
        # m>2090:A
        # rfg
    def __init__(self, nextWorkflow, condition):
        self.nextState = nextWorkflow
        self.condition = condition
        if condition is not None:
            self._letter = condition[0]
            self._isLargerThan = condition[1] == ">"
            self._number = int(condition[2:])
    def ConditionOk(self, machinepart):
        if self.condition is None:
            raise Exception("No condition")
        if self._isLargerThan:
            if self._letter == "x":
                return machinepart.x > self._number
            if self._letter == "m":
                return machinepart.m > self._number
            if self._letter == "a":
                return machinepart.a > self._number
            if self._letter == "s":
                return machinepart.s > self._number
        else:
            if self._letter == "x":
                return machinepart.x < self._number
            if self._letter == "m":
                return machinepart.m < self._number
            if self._letter == "a":
                return machinepart.a < self._number
            if self._letter == "s":
                return machinepart.s < self._number
    def __str__(self):
        if self.condition is None:
            return f"{self.nextState}"
        else:
            return f"if {self.condition} then {self.nextState}"       

class workflow:
    def __init__(self, name, rules):
        self.name = name
        self.rules = rules

    # Returns a machinepart with correct state, if we've reached an end state
    # Returns a workflow if we need to continue processing
    def process(self, machinepart):
        print(f"Processing {machinepart} with workflow '{self}'")
        for rule in self.rules:
            # Condition:NextState
            # NextState
            if rule.condition is None or rule.ConditionOk(machinepart):
                if rule.nextState == "A":
                    machinepart.accepted()
                    return machinepart
                if rule.nextState == "R":
                    machinepart.rejected()
                    return machinepart
                return rule.nextState
            
    def __str__(self):
        rulesString = ""
        for rule in self.rules:
            rulesString += f"{rule}, "
        return f"{self.name} {rulesString}"

class workflowEngine:
    def __init__(self, workflows):
        self.workflows = workflows
        for workflow in workflows:
            if workflow.name == "in":
                self.firstWorkflow = workflow
                break

    def processMachinePart(self, workflow, machinepart):
        workflowResult = workflow.process(machinepart)
        if isinstance(workflowResult, machinePart):
            return workflowResult
        else:
            nextWorkflow = None
            for workflow in self.workflows:
                if workflow.name == workflowResult:
                    nextWorkflow = workflow
                    break
            return self.processMachinePart(nextWorkflow, machinepart)

    def __str__(self):
        return f"Loaded with {len(self.workflows)} workflows. First workflow: {self.firstWorkflow}"

class machinePart:
    def __init__(self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s
        self.isAccepted = None
    def accepted(self):
        self.isAccepted = True
    def rejected(self):
        self.isAccepted = False
    def __str__(self):
        acceptedString = ""
        if self.isAccepted:
            acceptedString = "Accepted!"
        elif self.isAccepted == False:
            acceptedString = "Rejected!"
        return f"{acceptedString} X:{self.x} M:{self.m} A:{self.a} S:{self.s}"

# Example input: px{a<2006:qkq,m>2090:A,rfg}
def parseWorkflow(line):
    parts = line.replace('}', "").split("{")
    rules = []
    if len(parts) > 1:
        for r in parts[1].split(","):
            ruleDetails = r.split(":")
            if len(ruleDetails) > 1:
                # example: a<2006:qkq
                rules.append(rule(ruleDetails[1], ruleDetails[0]))
            else:
                rules.append(rule(ruleDetails[0], None))                # example: rfg        
    return workflow(parts[0].strip(), rules)

# Example input: {x=787,m=2655,a=1222,s=2876}
def parseMachinePart(line):
    line = line.replace("{", "").replace("}", "")
    parts = line.split(",")
    x = int(parts[0].split("=")[1])
    m = int(parts[1].split("=")[1])
    a = int(parts[2].split("=")[1])
    s = int(parts[3].split("=")[1])
    return machinePart(x, m, a, s)

def parseFile(lines):
    machineparts = []
    workflows = []
    for line in lines:
        if line.strip() == "":
            continue
        elif line[0:1] == '{':
            machineparts.append(parseMachinePart(line.strip()))
        else:
            workflows.append(parseWorkflow(line.strip()))
    return workflows, machineparts       

workflows, machineparts = parseFile(readFile("day19input.txt"))

for workflow in workflows:
    print(workflow)
for machinepart in machineparts:
    print(machinepart)

engine = workflowEngine(workflows)
print(engine)

xmasRating = 0
for machinepart in machineparts:
    sortedMachinePart = engine.processMachinePart(engine.firstWorkflow, machinepart)
    if sortedMachinePart.isAccepted:
        xmasRating += sortedMachinePart.x + sortedMachinePart.m + sortedMachinePart.a + sortedMachinePart.s
print(f"xmasRating: {xmasRating}")