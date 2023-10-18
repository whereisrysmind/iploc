import click

from src.ipstack import IPStackClient
from settings import settings


@click.command()
@click.argument('ipaddress')
def iploc(ipaddress):
    """This entrypoint allows quick retrieval of IP location information.
    Values returned as -> '{latitude} {longitude}'
    """
    ipstack_client = IPStackClient(settings)
    ip_info = ipstack_client.get_ipaddress_info(ipaddress)
    click.echo(f"{ip_info.latitude} {ip_info.longitude}")

if __name__ == '__main__':
    iploc()