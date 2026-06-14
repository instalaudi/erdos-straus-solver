import kagglesdk as ks

def automate_kaggle_kernel(kernel_name, notebook_path):
    # Authenticate with Kaggle API
    ks.authenticate()

    # Create a new kernel
    kernel_id = ks.kernels_create(notebook_path=notebook_path)

    # Initialize the kernel
    ks.kernels_initialize(kernel_id)

    # Run the kernel
    ks.kernels_run(kernel_id)

    # Retrieve logs
    logs = ks.kernels_logs(kernel_id)

    return logs

# Example usage
kernel_name = 'test_kernel'
notebook_path = 'path/to/notebook.ipynb'
logs = automate_kaggle_kernel(kernel_name, notebook_path)
print(logs)