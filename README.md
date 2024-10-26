# TrashNet Image Classification

## Project Overview

This project involves training a ResNet50 model to classify images of trash into different categories. The goal is to develop a robust image classification model that can accurately identify and categorize trash items, which can be useful for waste management and recycling efforts.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.11 installed. Then, install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download Dataset**:
   Download the TrashNet dataset and place it in the `dataset-resized` directory. The dataset should be organized into subdirectories for each class.

4. **Set Up Environment**:
   Ensure you have a CUDA-compatible GPU and the necessary drivers installed for PyTorch to utilize GPU acceleration.

## Usage

1. **Train the Model**:
   Open the Jupyter notebook `training-resnet50.ipynb` and run the cells to train the model. The notebook includes data preprocessing, model training, and evaluation steps.

2. **Evaluate the Model**:
   After training, the notebook provides functions to evaluate the model's performance on the validation and test datasets.

3. **Export Metrics**:
   Use the provided functions to export classification metrics and visualize accuracy per class.

## Model Details

- **Architecture**: The model is based on ResNet50, a deep residual network architecture known for its effectiveness in image classification tasks.
- **Dataset**: The TrashNet dataset, which includes images of various trash categories.
- **Preprocessing**: Images are resized to 224x224 pixels, with random horizontal flips and rotations applied for data augmentation.
- **Training**: The model is trained using cross-entropy loss and evaluated using accuracy, precision, recall, and F1 score metrics.

## Additional Information

- **Model Versioning**: The model is versioned and tracked using Weights & Biases (W&B).
- **Deployment**: The trained model is published on the Hugging Face Hub for easy access and deployment.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.