from django import template

register = template.Library()


@register.filter
def duration(value):
    hs, ms, ss = [int(i) for i in str(value).split(':')]

    def seconds(s):
        if s == 0:
            return '0 seconds'
        else:
            return '1 second' if s == 1 else '%d seconds' % s

    def minutes(s):
        if s == 0:
            return '0 minutes'
        else:
            return '1 minute' if s == 1 else '%d minutes' % s

    def hours(s):
        if s == 0:
            return '0 hours'
        else:
            return '1 hour' if s == 1 else '%d hours' % s

    if hs == 0:
        if ms == 0:
            return seconds(ss)
        else:
            if not ss == 0:
                return minutes(ms) + ' ' + seconds(ss)
            return minutes(ms)
    else:
        if ms == 0:
            if ss == 0:
                return hours(hs)
            else:
                return hours(hs) + ' ' + seconds(ss)
        else:
            if not ss == 0:
                return hours(hs) + ' ' + minutes(ms) + ' ' + seconds(ss)
            return hours(hs) + ' ' + minutes(ms)
