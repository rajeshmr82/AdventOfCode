import pytest
import puzzle

@pytest.fixture
def test_input():
    return """\
    px{a<2006:qkq,m>2090:A,rfg}
    pv{a>1716:R,A}
    lnx{m>1548:A,A}
    rfg{s<537:gd,x>2440:R,A}
    qs{s>3448:A,lnx}
    qkq{x<1416:A,crn}
    crn{x>2662:A,R}
    in{s<1351:px,qqz}
    qqz{s>2770:qs,m<1801:hdj,R}
    gd{a>3333:R,R}
    hdj{m>838:A,pv}

    {x=787,m=2655,a=1222,s=2876}
    {x=1679,m=44,a=2067,s=496}
    {x=2036,m=264,a=79,s=2244}
    {x=2461,m=1339,a=466,s=291}
    {x=2127,m=1623,a=2188,s=1013}
    """

def test_parse(test_input):
    pipeline, parts = puzzle.parse(test_input)
    assert len(pipeline.workflows) == 11  # 11 workflows defined
    assert len(parts) == 5  # 5 parts to evaluate
    assert parts[0] == {'x': 787, 'm': 2655, 'a': 1222, 's': 2876}  # Check first part

def test_calculate_sum(test_input):
    pipeline, parts = puzzle.parse(test_input)
    total_sum = puzzle.calculate_sum(pipeline, parts)
    assert total_sum == 19114  # Expected sum from the sample input

def test_solve_part_one(capsys):
    print('Solving Part One:')
    input_data = puzzle.read_input()
    answer = puzzle.solve_part_one(input_data)
    print(f'Part One : {answer}')
    assert 391132 == answer

def test_solve_part_two(capsys):
    print('Solving Part Two:')
    input_data = puzzle.read_input()
    answer = puzzle.solve_part_two(input_data)
    print(f'Part Two : {answer}')
    assert 128163929109524 == answer

def compare_workflows(workflow1, workflow2):
    # Convert each list of dictionaries to a set of frozen sets
    set1 = {frozenset(d.items()) for d in workflow1}
    set2 = {frozenset(d.items()) for d in workflow2}
    return set1 == set2

def test_translate_valid_workflows():
    original_workflows = {
        'px': ['a<2006:qkq', 'm>2090:A', 'rfg'],
        'pv': ['a>1716:R', 'A'],
        'lnx': ['m>1548:A', 'A'],
    }

    expected_output = {
        'px': [
            {'varname': 'a', 'operator': '<', 'operand': 2006, 'destiny': 'qkq'},
            {'varname': 'm', 'operator': '>', 'operand': 2090, 'destiny': 'A'},
            {'varname': '', 'operator': '', 'operand': 0, 'destiny': 'rfg'}
        ],
        'pv': [
            {'varname': 'a', 'operator': '>', 'operand': 1716, 'destiny': 'R'},
            {'varname': '', 'operator': '', 'operand': 0, 'destiny': 'A'}
        ],
        'lnx': [
            {'varname': 'm', 'operator': '>', 'operand': 1548, 'destiny': 'A'},
            {'varname': '', 'operator': '', 'operand': 0, 'destiny': 'A'}
        ],
    }

    translated_workflows = puzzle.translate_workflows(original_workflows)

    # Compare without considering order
    for wf_name, expected_conditions in expected_output.items():
        assert compare_workflows(translated_workflows[wf_name], expected_conditions)

def test_translate_workflow_with_no_conditions():
    original_workflows = {
        'empty': []
    }

    expected_output = {
        'empty': []
    }

    translated_workflows = puzzle.translate_workflows(original_workflows)
    assert compare_workflows(translated_workflows['empty'], expected_output['empty'])

def test_translate_workflow_with_mixed_conditions():
    original_workflows = {
        'mixed': ['a<1000:next', 'b>2000:R', 'next']
    }

    expected_output = {
        'mixed': [
            {'varname': 'a', 'operator': '<', 'operand': 1000, 'destiny': 'next'},
            {'varname': 'b', 'operator': '>', 'operand': 2000, 'destiny': 'R'},
            {'varname': '', 'operator': '', 'operand': 0, 'destiny': 'next'}
        ]
    }

    translated_workflows = puzzle.translate_workflows(original_workflows)
    assert compare_workflows(translated_workflows['mixed'], expected_output['mixed'])

def test_translate_workflow_with_workflow_name():
    original_workflows = {
        'workflow_name': ['rfg']  # Just a workflow name
    }

    expected_output = {
        'workflow_name': [
            {'varname': '', 'operator': '', 'operand': 0, 'destiny': 'rfg'}
        ]
    }

    translated_workflows = puzzle.translate_workflows(original_workflows)
    assert compare_workflows(translated_workflows['workflow_name'], expected_output['workflow_name'])

@pytest.mark.parametrize("expected_count", [167409079868000])
def test_count_accepted_combinations(test_input, expected_count):
    pipeline, parts = puzzle.parse(test_input)
    workflows = pipeline.workflows
    translated_workflows = puzzle.translate_workflows(workflows)
    accepted_count = puzzle.count_accepted_combinations(translated_workflows)
    assert accepted_count == expected_count