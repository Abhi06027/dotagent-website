import nextpy as xt


def categories_img(src):
    return xt.box(
        xt.image(src=src,),
    )


def categories():
    return xt.fragment(
        xt.box(
            xt.text(
                "Categories",
                class_name="lg:my-6 font-[DMSans] h6 lg:text-2xl my-2 text-lg md:my-4 md:text-[1.375rem] leading-8 text-[#E8ECEF] font-normal",
            ),
            xt.box(
                categories_img("/Interview.png"),
                categories_img("/books.png"),
                categories_img("/roleplaying.png"),
                categories_img("/automate.png"),
                categories_img("/news.png"),
                categories_img("/writeproof.png"),
                categories_img("/books.png"),
                categories_img("/roleplaying.png"),
                class_name="flex whitespace-nowrap overflow-x-scroll lg:overflow-x-hidden gap-4",
            ),
        ),
    )
