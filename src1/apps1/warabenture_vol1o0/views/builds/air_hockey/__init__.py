# BOF [O3o1o0g9o0]

from django.shortcuts import render


class AirHockeyView():
    """エアホッケー"""

    @staticmethod
    def render(request):
        """描画"""

        template_path = 'warabenture_vol1o0/Builds/AirHockey/index.html'
        #                ----------------------------------------------
        #                1
        # 1. `src1/apps1/warabenture_vol1o0/templates/warabenture_vol1o0/Builds/AirHockey/index.html` を取得
        #                                             ----------------------------------------------

        context = {}
        return render(request, template_path, context)

# EOF [O3o1o0g9o0]
