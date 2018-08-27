#
# First Flask Currency Dockerfile
#
#

#Pull base image.
FROM python:3.6.5

#Build commands
RUN easy_install pip
RUN mkdir /opt/currency_convertor
WORKDIR /opt/currency_convertor
ADD requirements.txt /opt/currency_convertor
RUN pip install -r requirements.txt
ADD . /opt/currency_convertor

# Define default command.
# CMD ["python", "api_conv_currency.py", "runserver"]
