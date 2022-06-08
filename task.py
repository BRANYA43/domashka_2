from random import randint


def get_distance(speed: int, time: int):
    distance = speed * time
    return distance


def get_position_on_track(distance: int, length_track: int):
    position = 0
    if distance > 0:
        if distance > length_track:
            position = distance - (distance // length_track * length_track)
        elif distance < length_track:
            position = distance

    elif distance < 0:
        if abs(distance) > length_track:
            position = distance - (distance // length_track * length_track)
        elif abs(distance) < length_track:
            position = length_track + distance

    return position


LENGTH_TRACK = 100
speed = 0
time = 0

message = ''

speed = int(input('Введіть швидкість руху(км): '))
time = int(input('Введіть час руху(год): '))

distance = get_distance(speed, time)
position = get_position_on_track(distance, LENGTH_TRACK)

if speed == 0:
    print('Васілій, не зможе зрушити з місця зі швидкістю 0км.')
if time == 0:
    print('Васілій, не скільки не пройде за час 0год')
elif time < 0:
    print('Не буває відємного часу')

if speed > 0:
    message = 'Васілій їхав за годиниковою стрілкою.\n'
elif speed < 0:
    message = 'Васілій їхав проти годиникової стрілки.\n'

message += f'Він проїхав {abs(distance)}км за {time}год та зупинився на позначці {position}км.'
print(message)
