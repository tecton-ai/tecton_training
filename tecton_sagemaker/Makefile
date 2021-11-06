all:

build:
	rm -f model-artifact.tar.gz
	dbfs cp --overwrite dbfs:/tmp/model/model.joblib model/
	cd model; tar czvf ../model-artifact.tar.gz .

put: build
	aws s3 cp model-artifact.tar.gz s3://tecton.ai.public/training/tecton_sagemaker/model-artifact.tar.gz
	aws s3api put-object-acl --bucket tecton.ai.public --key training/tecton_sagemaker/model-artifact.tar.gz


untar:
	@aws s3 ls s3://tecton.ai.public/training/tecton_sagemaker/model-artifact.tar.gz
	@aws s3 cp s3://tecton.ai.public/training/tecton_sagemaker/model-artifact.tar.gz .
	@rm -rf model
	@mkdir -p model
	@tar zxvf model-artifact.tar.gz --directory model
