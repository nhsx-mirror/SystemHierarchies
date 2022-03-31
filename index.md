<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>

# Open Statistics - Cyber Security



<div class="nhsuk-warning-callout">
  <h3 class="nhsuk-warning-callout__label">
    Important<span class="nhsuk-u-visually-hidden">:</span>
  </h3>
  <p>This project is currently in development. For more information please contact <a
                class="nhsuk-footer__list-item-link"
                href="{{ site.github.owner_url }}"
                >{{ site.github.owner_name }}</a>
   </p>
</div>

<div class="nhsuk-warning-callout">
  <h3 class="nhsuk-warning-callout__label">
    Important<span class="nhsuk-u-visually-hidden">:</span>
  </h3>
  <p>This project is currently in development. For more information please contact <a href="mailto:muhammad-faaiz.shanawas@nhsx.nhs.uk">muhammad-faaiz.shanawas@nhsx.nhs.uk</a>. <br>This is an exploratory piece leveraging open source data and widget tooling in R - it has not received formal QA. <br>Opinions expressed in this page are not representative of the views of NHSX and any content here should not be regarded as official output in any form. For more information about NHSX please visit our <a href="https://www.nhsx.nhs.uk/">official website.</a>.
   </p>
</div>



<br>
# Funnel Chart
<br>
Funnel chart showing the number of organisations at each stage starting with Regions at the top and GP practices at the bottom.

{% include funnel_chart.html %}

# Sunburst Chart - Regions -> ICS -> CCGs -> PCNs -> GP Practices
<br>
Sunburst chart showing the mapping of each region through to GP practices. Clicking on each sector expands this selection.

<iframe src="sunburst_large.html" height="600px" width="100%" style="border:none;"></iframe>

<hr class="nhsuk-u-margin-top-0 nhsuk-u-margin-bottom-6">


# Suburst Chart - Regions -> ICSs -> CCGs
Sunburst chart showing the mapping of each region through to CCGs. Clicking on each sector expands this selection.

<iframe src="sunburst_small.html" height="600px" width="100%" style="border:none;"></iframe>

<hr class="nhsuk-u-margin-top-0 nhsuk-u-margin-bottom-6">


# Tree Map - Regions -> ICS -> CCGs -> PCNs -> GP Practices
Tree map containing the hierarchy mapping regions through to GP practices. Clicking on each of the rectangles expands this selection.

<iframe src="treemap_small.html" height="600px" width="100%" style="border:none;"></iframe>

<hr class="nhsuk-u-margin-top-0 nhsuk-u-margin-bottom-6">


# Tree Map - Regions -> ICS -> CCGs
Tree map contianing the hierarchy mapping regions through to CCGs. Clicking on each of the rectangles expands this selection.

<iframe src="treemap_large.html" height="600px" width="100%" style="border:none;"></iframe>

<hr class="nhsuk-u-margin-top-0 nhsuk-u-margin-bottom-6">

Template for end-to-end open source analytics: [github.io](https://pages.github.com/), and [github actions](https://github.com/features/actions).

Analytics leverages open source data and R libraries such as [leaflet](https://cran.r-project.org/web/packages/leaflet/index.html) for interactive maps, [plotly](https://plotly.com/r/) for other interactive visualisations and [summarytools](https://cran.r-project.org/web/packages/summarytools/vignettes/introduction.html) for descriptive statistics.