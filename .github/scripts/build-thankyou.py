from fastcore.all import *
from ghapi.all import *
import json

def reply_thanks():
    api = GhApi(owner='tcapelle', repo='pr_action', token=github_token())
    payload = context_github.event
    if 'workflow' in payload: issue = 1
    else:
        if payload.action != 'opened': return
        issue = payload.number
    try:
        resp = api.issues.create_comment(issue_number=issue, body='Thank you for your *valuable* contribution')
        print(f"post comment correctly with reply: {resp}")
    except BaseException as exc:
        print(f"Failed to post comment")
        try:
            result_body = json.loads(exc.fp.read())
            print(f"Result body from github: {result_body}")
        except BaseException as inner_exc:
             print(f"Tried to get result body from Github, but was unsuccessful")
        raise exc

reply_thanks()