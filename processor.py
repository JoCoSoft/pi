import sched
import time
import requests
import motor

delay = 5
priority = 1
scheduler = sched.scheduler(time.time, time.sleep)


def processJobs():
    print "--- processJobs() ---"
    processJobsUrl = "http://jocosoft-api.herokuapp.com/api/v1/jobs/process"  # PROD
    # processJobsUrl = "http://localhost:3000/api/v1/jobs/process"  # DEV

    response = requests.post(processJobsUrl, json={
        "serial": "dev-vent", "code": "123456"})  # Pull serial / code from some storage
    jsonResponse = response.json()

    for job in jsonResponse:
        print "Processing job " + job["id"]
        jobName = job["name"]
        jobDegrees = 90

        try:
            jobDegrees = job["data"]["degrees"]
        except KeyError:
            pass

        if jobName == "open":
            motor.openVent(jobDegrees)
            continue

        if jobName == "close":
            motor.closeVent(jobDegrees)
            continue


def processJobScheduler(_scheduler):
    print "--- processJobScheduler() ---"
    processJobs()
    scheduler.enter(delay, priority, processJobScheduler, (_scheduler,))


def main():
    print "--- main ----"
    processJobs()
    scheduler.enter(delay, priority, processJobScheduler, (scheduler,))
    scheduler.run()


if __name__ == "__main__":
    main()
