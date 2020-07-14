from rest_framework.decorators import api_view
from rest_framework.response import Response

from collections import Counter

@api_view(['POST'])
def lambda_function(request):
    data = Counter(request.data.get('question'))

    solution = []

    for item in data.most_common():
        for _ in range(item[1]):
            solution.append(item[0])

    return Response({
        'solution': solution
    }) 
