import logging.config
import click
from spamcannon.logconf import LOGCONF
from spamcannon.cannon import send_requests

logger = logging.getLogger(__file__)
logging.config.dictConfig(LOGCONF)


@click.command()
@click.option('-v', '--volley', default=10, help='Number of requests to send at a time')
@click.option('-s', '--silent', is_flag=True, help="Run silently i.e. don't log anything")
def spam(volley, silent):
    """Send spam requests to some douche bags server"""

    total_errors = 0
    total_requests = 0

    while True:
        try:
            error_count = send_requests(volley)
        except KeyboardInterrupt:
            break
        else:
            total_errors += error_count
            total_requests += volley

            totals = f'requests: {total_requests}, errors: {error_count}'
            rates = f'err rate: {error_count / volley:.02f}, avg err rate: {total_errors / total_requests:.02f}'
            report = f'{totals}, {rates}'
            if not silent:
                logger.info(report)

            if error_count == volley:
                logger.info('mission accomplished: you crashed his server lol')
                break


spam()
