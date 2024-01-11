import nextpy as xt


def favoritecharacters():
    return xt.fragment(
        xt.box(
            xt.text(
                "Talk to your favorite characters",
                class_name="lg:my-6 font-DMSans h6 lg:text-2xl my-2 text-lg md:my-4 md:text-[1.375rem] leading-8 text-[#E8ECEF] font-normal",
            ),
            xt.box(
                xt.image(
                    src="/study.jpg",
                    class_name="w-12 h-12 rounded-xl",
                ),
                xt.box(
                    xt.text(
                        "Alternate Timelines",
                        class_name="text-sm font-DMSans font-medium text-[#fefefe] leading-6",
                    ),
                          xt.text(
                        "Try saying:",
                        class_name="text-xs italic font-DMSans font-medium leading-4 text-[#E5E0D8] opacity-80 relative",
                    ),
                ),
                class_name="flex space-x-2 items-center",
            ),
        ),
    )