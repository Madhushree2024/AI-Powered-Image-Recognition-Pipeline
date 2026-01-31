const handleUploadAndLiveTrack = async (file) => {
  // 1. Upload to S3 (Use AWS Amplify or a Presigned URL)
  const fileName = `${Date.now()}-${file.name}`;
  await uploadToS3(fileName, file); 

  // 2. Start Polling for results
  const interval = setInterval(async () => {
    const res = await fetch(`https://l7vhs0u7td.execute-api.us-east-1.amazonaws.com/prod/results?id=${fileName}`);
    const data = await res.json();
    
    if (data.Labels) { // If labels exist, processing is done!
      setResults(data.Labels);
      clearInterval(interval);
    }
  }, 2000); 
};