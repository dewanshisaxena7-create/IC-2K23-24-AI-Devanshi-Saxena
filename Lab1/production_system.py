
def production_system():
    """Demonstrate a simple rule-based production system."""

    facts = {"has_fever", "has_cough"}

    rules = [
        ({"has_fever", "has_cough"}, "possible_flu"),
        ({"possible_flu"}, "consult_doctor"),
    ]

    print("Initial Facts:", facts)

    changed = True
    while changed:
        changed = False

        for conditions, conclusion in rules:
            if conditions.issubset(facts) and conclusion not in facts:
                facts.add(conclusion)
                print(f"Rule Fired: {conditions} -> {conclusion}")
                print("New Fact:", conclusion)
                changed = True

    print("\nFinal Facts:", facts)


if __name__ == "__main__":
    production_system()
