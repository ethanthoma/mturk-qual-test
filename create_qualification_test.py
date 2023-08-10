import boto3


def main():
    questions = open('questions.xml').read()
    answers = open('answer_key.xml').read()

    mturk = boto3.client('mturk',
                         endpoint_url='https://mturk-requester.us-east-1.amazonaws.com/',
                         # endpoint_url='https://mturk-requester-sandbox.us-east-1.amazonaws.com/',
                         region_name='us-east-1')

    # Create the qualification type
    qual_response = mturk.create_qualification_type(
        Name='Generated Sentence Quality Evaluation',
        Keywords='nlp, commongen, generations',
        Description='The worker is qualified to answer HITs about fluency, sensibility, and complexity for generated sentences.',
        RetryDelayInSeconds=172800,
        QualificationTypeStatus='Active',
        Test=questions,
        AnswerKey=answers,
        TestDurationInSeconds=300
    )

    print(qual_response['QualificationType']['QualificationTypeId'])


if __name__ == '__main__':
    main()
