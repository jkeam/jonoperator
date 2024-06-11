FROM registry.access.redhat.com/rhel9/python-312@sha256:884310589ce80d48960c81ad08b71ccc184babfd02e768e792ab01f649d5b3fa
ADD ./requirements.txt .
RUN pip install -r requirements.txt
ADD . .
CMD kopf run /src/handlers.py --verbose
