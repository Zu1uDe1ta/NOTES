{"username":"chrischavez","key":"0acbcb63f1e3e3d082611ec77ac97d42"}

mkdir /Users/cchavez/.kaggle

/Users/cchavez/dev/airflow_home/.kaggle

/Users/cchavez/dev/airflow_home/kaggle/kaggle_token.json

cp /Users/psehgal/kaggle.json Users/psehgal/.kaggle


kaggle datasets download -d jordangoblet/atp-tour-20002016

kaggle competitions download -c house-prices-advanced-regression-techniques


$cp /Users/cchavez/dev/airflow_home/kaggle/kaggle_token.json Users/cchavez/.kaggle




    Task_III = PythonOperator(
        task_id="write_questions_to_s3", python_callable=write_questions_to_s3
    )

    Task_IV = PythonOperator(
        task_id="render_template",
        python_callable=render_template,
        provide_context=True,
    )

    Task_V = EmailOperator(
        task_id="send_email",
        provide_context=True,
        to="my_email@mail.com",
        subject="Top questions with tag 'pandas' on {{ ds }}",
        html_content="{{ task_instance.xcom_pull(task_ids='render_template', key='html_content') }}",
    )