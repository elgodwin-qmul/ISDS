import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_comparison_summary(
    df,
    year_col,
    group1_col,
    group2_col,
    group1_label,
    group2_label,
    title,
    figsize=(14, 7),
    save_path=None,
    show_table=False
):

    # -----------------------------------
    # TOTALS
    # -----------------------------------

    total_group1 = df[group1_col].sum()
    total_group2 = df[group2_col].sum()

    total_pct = (
        total_group1 /
        (total_group1 + total_group2)
    ) * 100

    # -----------------------------------
    # X POSITIONS
    # -----------------------------------

    years = df[year_col].astype(str)

    x_years = np.arange(len(years))

    x_total = len(years) + 1

    # -----------------------------------
    # FIGURE
    # -----------------------------------

    fig, ax1 = plt.subplots(figsize=figsize)

    # -----------------------------------
    # LEFT AXIS
    # -----------------------------------

    ax1.bar(
        x_years,
        df[group1_col],
        label=group1_label
    )

    ax1.bar(
        x_years,
        df[group2_col],
        bottom=df[group1_col],
        label=group2_label,
        alpha=0.75
    )

    ax1.set_ylabel("Annual Number of Cases")

    # -----------------------------------
    # ANNOTATE YEARLY %
    # -----------------------------------

    for i, row in df.iterrows():

        total_height = (
            row[group1_col] +
            row[group2_col]
        )

        pct = (
            row[group1_col] /
            total_height
        ) * 100

        ax1.text(
            x_years[i],
            total_height + 1,
            f"{pct:.1f}%",
            ha="center",
            va="bottom",
            fontsize=9,
            fontweight="bold",
            rotation=90
        )

    # -----------------------------------
    # RIGHT AXIS
    # -----------------------------------

    ax2 = ax1.twinx()

    ax2.bar(
        x_total,
        total_group1
    )

    ax2.bar(
        x_total,
        total_group2,
        bottom=total_group1,
        alpha=0.75
    )

    ax2.set_ylabel(
        "Total Number of Cases",
        rotation=-90,
        labelpad=15
    )

    # -----------------------------------
    # TOTAL %
    # -----------------------------------

    total_height = total_group1 + total_group2

    ax2.text(
        x_total,
        total_height + (0.02 * total_height),
        f"{total_pct:.1f}%",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold",
        rotation=90
    )

    # -----------------------------------
    # SEPARATOR
    # -----------------------------------

    ax1.axvline(
        x=len(years) - 0.5,
        linestyle="--",
        alpha=0.7,
        color="black"
    )

    # -----------------------------------
    # X LABELS
    # -----------------------------------

    xticks = list(x_years) + [x_total]
    xlabels = list(years) + ["Total"]

    ax1.set_xticks(xticks)
    ax1.set_xticklabels(
        xlabels,
        rotation=45,
        ha="right"
    )

    # -----------------------------------
    # TITLE + LEGEND
    # -----------------------------------

    ax1.set_title(title)

    ax1.legend(loc="upper left")

    # -----------------------------------
    # Y LIMITS
    # -----------------------------------

    left_max = (
        df[group1_col] +
        df[group2_col]
    ).max()

    ax1.set_ylim(0, left_max * 1.15)

    right_max = total_group1 + total_group2

    ax2.set_ylim(0, right_max * 1.15)

    plt.tight_layout()

    if save_path:

        plt.savefig(
            save_path,
            dpi=600,
            bbox_inches="tight"
        )
    plt.show()

    # -----------------------------------
    # SUMMARY TABLE
    # -----------------------------------

    if show_table:

        summary_table = df.copy()

        summary_table["total_cases"] = (
            summary_table[group1_col] +
            summary_table[group2_col]
        )

        summary_table["percentage"] = (
            summary_table[group1_col] /
            summary_table["total_cases"] * 100
        ).round(1)

        total_row = pd.DataFrame({
            year_col: ["Total"],
            group1_col: [total_group1],
            group2_col: [total_group2],
            "total_cases": [summary_table["total_cases"].sum()],
            "percentage": [round(total_pct, 1)]
        })

        summary_table = pd.concat(
            [summary_table, total_row],
            ignore_index=True
        )

        return summary_table


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_yearly_totals(
    df,
    year_col,
    value_col,
    title,
    bar_color="#1f77b4",
    total_color="#ff7f0e",
    figsize=(14, 7),
    save_path=None,
    show_table=False
):

    # -----------------------------------
    # OVERALL TOTAL
    # -----------------------------------

    grand_total = df[value_col].sum()

    # -----------------------------------
    # X POSITIONS
    # -----------------------------------

    years = df[year_col].astype(str)

    x_years = np.arange(len(years))

    x_total = len(years) + 1

    # -----------------------------------
    # FIGURE
    # -----------------------------------

    fig, ax1 = plt.subplots(figsize=figsize)

    # -----------------------------------
    # LEFT AXIS:
    # YEARLY TOTALS
    # -----------------------------------

    ax1.bar(
        x_years,
        df[value_col],
        color=bar_color
    )

    ax1.set_ylabel("Annual Number of Cases")

    # -----------------------------------
    # ANNOTATE YEARLY TOTALS
    # -----------------------------------

    for i, row in df.iterrows():

        ax1.text(
            x_years[i],
            row[value_col] + 1,
            f'{row[value_col]}',
            ha="center",
            va="bottom",
            fontsize=9,
            fontweight="bold",
            rotation=90
        )

    # -----------------------------------
    # RIGHT AXIS:
    # GRAND TOTAL
    # -----------------------------------

    ax2 = ax1.twinx()

    ax2.bar(
        x_total,
        grand_total,
        color=total_color
    )

    ax2.set_ylabel(
        "Total Number of Cases",
        rotation=-90,
        labelpad=15
    )

    # -----------------------------------
    # ANNOTATE GRAND TOTAL
    # -----------------------------------

    ax2.text(
        x_total,
        grand_total + (0.02 * grand_total),
        f"{grand_total}",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold",
        rotation=90
    )

    # -----------------------------------
    # SEPARATION LINE
    # -----------------------------------

    ax1.axvline(
        x=len(years) - 0.5,
        color="black",
        linestyle="--",
        alpha=0.7
    )

    # -----------------------------------
    # X-AXIS LABELS
    # -----------------------------------

    xticks = list(x_years) + [x_total]
    xlabels = list(years) + ["Total"]

    ax1.set_xticks(xticks)

    ax1.set_xticklabels(
        xlabels,
        rotation=45,
        ha="right"
    )

    # -----------------------------------
    # TITLE
    # -----------------------------------

    ax1.set_title(title)

    # -----------------------------------
    # EXPAND Y LIMITS
    # -----------------------------------

    left_max = df[value_col].max()

    ax1.set_ylim(0, left_max * 1.15)

    ax2.set_ylim(0, grand_total * 1.15)

    plt.tight_layout()

    if save_path:

        plt.savefig(
            save_path,
            dpi=600,
            bbox_inches="tight"
        )

    plt.show()

    # -----------------------------------
    # SUMMARY TABLE
    # -----------------------------------

    if show_table:

        total_row = pd.DataFrame({
            year_col: ["Total"],
            value_col: [grand_total]
        })

        summary_table = pd.concat(
            [df, total_row],
            ignore_index=True
        )

        return summary_table