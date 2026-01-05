
# 👁️ AI-Powered Image Recognition Pipeline (AWS Rekognition)

An event-driven, serverless machine learning pipeline that automatically identifies objects in images upon upload. This project demonstrates a cloud-native architecture for real-time data processing and AI integration.

---

## 📌 Project Overview
The goal of this project was to build a fully automated system that processes images without manual intervention. By using an **event-driven** approach, the system remains idle (costing $0) until a file is uploaded to S3, which instantly triggers a serverless workflow to analyze the image and store the metadata.

### Key Capabilities:
* **Event-Driven Ingestion**: Real-time processing triggered by S3 bucket events.
* **Computer Vision**: Automated labeling of images using AWS Rekognition.
* **Sub-Second Latency**: Optimized Python Lambda function achieving end-to-end processing in ~500-800ms.
* **Persistence**: Structured metadata storage in DynamoDB for easy downstream querying.

---

## 🛠️ Technical Stack
* **Cloud Provider**: AWS (Amazon Web Services)
* **Intelligence**: AWS Rekognition (Deep Learning-based Image Analysis)
* **Compute**: AWS Lambda (Python 3.12)
* **Storage**: Amazon S3
* **Database**: Amazon DynamoDB
* **Monitoring**: Amazon CloudWatch
* **SDK**: Boto3

---

## 🏗️ Architecture & Workflow
1.  **S3 Bucket**: A user uploads an image (JPG/PNG).
2.  **S3 Event**: S3 sends a notification to AWS Lambda.
3.  **Lambda Function**: The Python-based "Brain" extracts the image info and calls Rekognition.
4.  **Rekognition API**: Analyzes the image and returns a list of detected objects (Labels) with confidence scores.
5.  **DynamoDB**: The Lambda function saves the image name and the detected labels into a NoSQL table.



---

## 📊 Proof of Work (Verified Jan 4, 2026)
* **Performance**: CloudWatch logs confirm a total execution duration of **< 1 second** per image.
* **Scalability**: Tested with multiple concurrent uploads; Lambda scaled automatically to handle the load.
* **Precision**: Configured a `MinConfidence` threshold of **80%** to ensure high-quality metadata.

---

## 📁 Repository Structure
```text
├── src/
│   └── lambda_function.py      # Python script for image processing
├── assets/
│   ├── s3-upload.png           # Screenshot of input image in S3
│   ├── lambda-config.png       # Screenshot of S3-Lambda trigger
│   └── dynamodb-output.png     # Screenshot of detected labels in DB
└── README.md                   # Detailed project documentation


```
## 📝 Setup & Deployment
* 1. Database: Create a DynamoDB table named ImageLabels with ImageID as the primary key.

* 2.Permissions: Attach a policy to the Lambda IAM Role allowing s3:GetObject, rekognition:DetectLabels, and dynamodb:PutItem.

* 3. Trigger: Configure an S3 Bucket notification to trigger the Lambda function on All object create events.

* 4. Test: Upload an image to the bucket and refresh your DynamoDB table to see the AI results!

## 📖 How it Works
1.  An image is uploaded to the designated **S3 Bucket**.
2.  An **S3:ObjectCreated** event triggers the **Lambda function**.
3.  The Lambda function extracts the bucket name and object key.
4.  The function sends the image to **AWS Rekognition**.
5.  Detected labels with a confidence score > 80% are parsed.
6.  The image id and its corresponding labels are saved into **DynamoDB**.

## 📊 Performance Monitoring
Using **Amazon CloudWatch**, I monitored the performance of the pipeline.
* **Average Execution Time:** ~450ms - 700ms
* **Memory Footprint:** ~60MB - 80MB
* **Success Rate:** 100% (based on test image sets)
