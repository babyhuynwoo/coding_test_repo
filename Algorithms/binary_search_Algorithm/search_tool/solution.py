import sys

def search_tool(repo, request):
    result = []
    for item in request:
        if item in repo:
            result.append('yes')
        else:
            result.append('no')
    return result