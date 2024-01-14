import nextpy as xt


def bubble():
    return xt.box(
        xt.box(
            xt.box(
                xt.text(
                    "Access to my own personal time machine",
                    class_name="text-sm pl-5 py-4 my-4 text-white leading-[1.125rem] font-[DMSans] font-normal lg:w-60	w-72",
                ),
                style={
                    "position": "relative",
                    "font-family": "sans-serif",
                    "background": "#343839",
                    "border-radius": "15px",
                    "::before": {
                        "position": "absolute",
                        "width": "0",
                        "height": "0",
                        "left": "auto",
                        "right": "-15px",
                        "top": "39px",
                        "bottom": "auto",
                        "border": "12px solid",
                        "border-color": "#343839 transparent transparent #343839",
                        "border-radius": "10px",
                    },
                },
            ),
        ),
    )


def teach(src):
    return xt.box(
        xt.box(
            xt.image(
                src=src,
                class_name="w-12 h-12 rounded-xl",
            ),
            xt.box(
                xt.text(
                    "Alternate Timelines",
                    class_name="text-sm font-[DMSans] font-medium text-[#fefefe] leading-6",
                ),
                xt.text(
                    "Try saying:",
                    class_name="text-xs italic font-[DMSans] font-medium leading-4 text-[#E5E0D8] opacity-80 relative",
                ),
            ),
            class_name="flex space-x-2 items-center",
        ),
    )


def favoritecharacters():
    return xt.fragment(
        xt.box(
            xt.text(
                "Talk to your favorite characters",
                class_name="lg:my-6 font-[DMSans] h6 lg:text-2xl my-2 text-lg md:my-4 md:text-[1.375rem] leading-8 text-[#E8ECEF] font-normal",
            ),
            xt.box(
                xt.box(
                    xt.box(
                        teach("/study.jpg"),
                        bubble(),
                        bubble(),
                        bubble(),
                    ),
                ),
                xt.box(
                    teach("/study.jpg"),
                    bubble(),
                    bubble(),
                    bubble(),
                ),
                xt.box(
                    teach("/study.jpg"),
                    bubble(),
                    bubble(),
                    bubble(),
                ),
                xt.box(
                    teach("/study.jpg"),
                    bubble(),
                    bubble(),
                    bubble(),
                ),
                xt.box(
                    teach("/study.jpg"),
                    bubble(),
                    bubble(),
                    bubble(),
                ),
                xt.box(
                    teach("/study.jpg"),
                    bubble(),
                    bubble(),
                    bubble(),
                ),
                class_name="flex space-x-5 overflow-x-scroll lg:overflow-x-hidden ",
            ),
        ),
    )
