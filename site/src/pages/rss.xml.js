import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context) {
  const posts = (await getCollection('insights'))
    .filter((p) => !p.data.draft)
    .sort((a, b) => b.data.date.getTime() - a.data.date.getTime());

  return rss({
    title: 'Gad Sosa — Insights',
    description: 'Writing on machine-learning security, scaling engineering teams, and technology leadership.',
    site: context.site,
    items: posts.map((post) => ({
      title: post.data.title,
      pubDate: post.data.date,
      description: post.data.description,
      link: `/insights/${post.id}/`,
      categories: [post.data.tag],
    })),
    customData: '<language>en-us</language>',
  });
}
