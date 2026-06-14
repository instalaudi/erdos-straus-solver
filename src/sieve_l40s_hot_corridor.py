import deepseek_verifier

# ... existing code ...

def process_results(results):
    # ... existing code ...
    top_n_results = get_top_n_results(results)
    verification_results = deepseek_verifier.verify(top_n_results)
    append_to_kaggle_output(verification_results)
