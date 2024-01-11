import nextpy as xt


def categories():
    return xt.fragment(
        xt.box(
            xt.text(
                "Categories",
                class_name="lg:my-6 font-DMSans h6 lg:text-2xl my-2 text-lg md:my-4 md:text-[1.375rem] leading-8 text-[#E8ECEF] font-normal",
            ),
            xt.box(
                xt.image(
                    src="/Interview.png",
                    class_name="min-w-[9.375rem]",
                ),
                xt.image(
                    src="/books.png",
                    class_name="min-w-[9.375rem]",
                ),
                xt.image(
                    src="/roleplaying.png",
                    class_name="min-w-[9.375rem]",
                ),
                xt.image(
                    src="/automate.png",
                    class_name="min-w-[9.375rem]",
                ),
                xt.image(
                    src="/news.png",
                    class_name="min-w-[9.375rem]",
                ),
                xt.image(
                    src="/writeproof.png",
                    class_name="min-w-[9.375rem]",
                ),
                xt.image(
                    src="/books.png",
                    class_name="min-w-[9.375rem]",
                ),
                xt.image(
                    src="/roleplaying.png",
                    class_name="min-w-[9.375rem]",
                ),
                class_name="flex whitespace-nowrap overflow-x-scroll lg:overflow-x-hidden	 gap-4 ",
            ),
        ),
    )
