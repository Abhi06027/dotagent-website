import nextpy as xt


def all_agents_img():
    return xt.box(
        xt.box(
            xt.box(
                xt.image(src="/AllAgentsCard.png", class_name="w-52 h-28"),
            ),
            xt.box(
                xt.text(
                    "Mobile Legends: Bang Bang",
                    class_name="lg:text-2xl text-[1.3rem] font-[DMSans] font-medium leading-6 text-white",
                ),
                xt.text(
                    "Play with the world!....",
                    class_name="text-xs py-2 text-white font-[DMSans]",
                ),
                xt.box(
                    xt.box(
                        "Get",
                        class_name="flex items-center border-0 rounded-3xl max-h-[1.38rem] tracking-normal font-[DMSans] px-6 py-4 bg-[#8e55ea] text-white lg:text-lg text-base",
                    ),
                    xt.image(
                        src="/ShareButton.png",
                        class_name="w-10 h-9",
                    ),
                    class_name="flex justify-between gap-20 items-center mt-4 md:mt-1",
                ),
                class_name="flex flex-col ",
            ),
            class_name="flex gap-4",
        ),
        class_name="md:p-5 p-3 bg-[#1b1e1f]  my-4 rounded-3xl",
    )


def all_agents():
    return xt.fragment(
        xt.box(
            xt.text(
                "All agents",
                class_name="lg:my-6 font-[DMSans] h6 lg:text-2xl my-2 text-lg md:my-4 md:text-[1.375rem] leading-8 text-[#E8ECEF] font-normal",
            ),
            xt.box(
                xt.box(
                    all_agents_img(),
                    all_agents_img(),
                ),
                xt.box(
                    all_agents_img(),
                    all_agents_img(),
                ),
                class_name="flex lg:flex-row flex-col justify-between gap-5",
            ),
        ),
    )
