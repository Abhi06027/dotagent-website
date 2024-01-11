# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts.
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

import nextpy as xt
from dotagent_website.components.banner import banner
from dotagent_website.components.categories import categories
from dotagent_website.components.Interviewprep import Interviewprep
from dotagent_website.components.favoritecharacters import favoritecharacters


# Construct the filename to display
from xtconfig import config

filename = f"{config.app_name}/{config.app_name}.py"


# define index page. Frontend Pages are just functions that return a frontend components
def navbar():
    return xt.box(
        xt.box(
            xt.image(
                src="/top.png",
                class_name="w-6",
            ),
            xt.image(
                src="/newlogo.png",
                class_name="w-8 h-8",
            ),
            xt.text(
                "dot.agent",
             
                class_name="relative font-Poppins font-extrabold  bg-clip-text text-transparent bg-gradient-to-l from-[#ED5FC4] to-[#4123E6]",
            ),
            class_name="flex gap-4 items-center",
        ),
        xt.box(
            xt.box(
                xt.box(
                    xt.image(
                        src="/Frame1.svg",
                    ),
                    class_name="absolute inset-y-0 left-0 flex items-center pl-4",
                ),
                xt.input(
                    placeholder="Ask the smartest AI agent",
                    variant="unstyled",
                    class_name="lg:w-80 w-64 p-3 pl-12 font-sans font-normal text-base md:block hidden font-DMSans text-[#6C7275] placeholder-[#6C7275] rounded-xl bg-red-500",
                ),
                class_name="relative",
            ),
            xt.box(
                xt.text("Share", class_name="hidden md:block"),
                xt.image(
                    src="/share-06.svg",
                    class_name="w-5	h-5 ",
                ),
                class_name="bg-[#F1F5F9] text-[#292D32] font-medium font-DMSans flex gap-2 justify-center items-center  w-11 h-11 md:w-24 md:h-full  md:px-6 py-2.5	 md:rounded-[2.5rem] rounded-full ",
            ),
            xt.box(
                xt.image(
                    src="/avatar.png",
                ),
                class_name="bg-[#C2E281] w-11 h-11  rounded-full  ",
            ),
            class_name="flex items-center justify-center   gap-5",
        ),
        class_name="flex items-center justify-between bg-[#141718] py-2 px-4",
    )


def index() -> xt.Component:
    return xt.fragment(
        xt.box(
            navbar(),
            xt.box(
                xt.box(
                    banner(),
                    categories(),
                    Interviewprep(),
                    favoritecharacters(),
                    class_name=" md:mx-12 mx-6",
                ),
                   class_name="sm:ml-0 md:ml-0 bg-[#232627] overflow-hidden flex flex-col pt-6 pb-4 md:pb-18 rounded-[1.25rem]",
            ),
            class_name="bg-[#141718] h-full",
        ),
    )


app = xt.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Poppins&display=swap",
    ],
)
app.add_page(index)
