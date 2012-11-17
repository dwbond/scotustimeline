Supreme Court of the United States Timeline

Renders a timeline of the Supreme Court's decisions.

Work items:

Wrote method to return list of time intervals. Now need to query database for the cases from the time periods in the list, and then to pull the two highest ranked cases from the cases for the set time period.

These two cases then need to be displayed on timeline.html, which serves as the home page for the site, one below, one above. This will require Bootstrap. Each case takes up two grid sections on the Bootstrap scaffold.

The next step will be to introduce fields for users to modify the scale of the timeline. These changes need to be passed back to timespan to determine the new intervals, and the page will have to be reloaded with the new timeline. Hopefully there will eventually be a way to do that on the page without refreshing it, but I don't plan to do that anytime soon.

After this, I can start to implement some of the other fields of Case, which will lay the foundation for filtering the timeline based on customized user queries.
