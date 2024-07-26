# Swiss Pine Technology - Exam
This Repository is intended for technical exam required from the Organization in [SwissPine Technology](https://swisspinetech.com/) and this will by my Entry as an applicant


# Problem Statement
The assessment includes challenges across the whole stack that the client is using as follows:
- CI/CD
- Docker/Kubernetes
- Infrastructure as Code
- Web server coding

# User Acceptance Criteria
- Must have and endpoint for */api/health* for health checking with payload 

    ```json
    { "status": "ok" }
    ```
- Has and endpoint for **/api/mirror?word={word} with this function as follows:
    * Any lowercase letter must be transformed to be uppercase
    * Any uppercase letter must be transformed to be lowercase
    * Any other character should be left as is
    * . A final transformation must be applied so that the whole string is reversed. (’foo’ ⇒ ‘oof’, ‘bar’ ⇒ ‘rab’)
    * Sample endpoint */api/mirror?word=fOoBar25*
    ```json
    { "transformed": "52RAbOoF" }
    ```
- The  It saves the the pair <word, mirroredWord> in a database
- Build the main branch and push to docker registry
- Orchestrate Cluster Deployment
- Ensure Pass All Test
- Create Infrastructure as Code
- Create Pipeline as Code