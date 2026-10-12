FROM python:2.7
RUN pip install distorm3==3.4.4 pycryptodome && \
    git clone --depth 1 https://github.com/volatilityfoundation/volatility.git /opt/volatility && \
    git clone --depth 1 https://github.com/superponible/volatility-plugins.git /opt/volatility-plugins && \
    printf '#!/bin/sh\nexec python2 /opt/volatility/vol.py "$@"\n' > /usr/local/bin/volatility && chmod +x /usr/local/bin/volatility
WORKDIR /memlabs
