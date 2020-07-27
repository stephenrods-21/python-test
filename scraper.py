from twitter_scraper import Profile


def get_account_name_from_url(twitter_url):
    account_name = twitter_url.replace('https://twitter.com/', '')
    return account_name


if __name__ == '__main__':
    url = input('Enter the twitter profile url\n')
    account_name = get_account_name_from_url(url)

    try:
        profile = Profile(account_name)
        print('@{0} has {1:,} Followers on Twitter'.format(account_name, profile.followers_count))
    except IndexError:
        print('No Profile found!')
